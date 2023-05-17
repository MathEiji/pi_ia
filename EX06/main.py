import discord
import requests
import tensorflow as tf
import cv2
import imageio.v3 as iio

class_names = ["Angry", "Happy", "Sad", "Surprise"]

def detect_emotion(frame):
    model = tf.keras.models.load_model("model_v2.h5")
    emotion = list(model.predict(tf.expand_dims(frame, axis=0)))
    num = max(emotion[0])
    idx = list(emotion[0]).index(num)
    return idx, num


def preprocess(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (48, 48))
    frame = frame / 255.

    return frame


def detect_face(frame):
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return gray, frame, faces
 
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    a_id = message.author.id
    if message.author.id != 1100544229895327904:
        if len(message.attachments) > 0:
            # Getting image
            x = message.attachments[0].url
            frame = requests.get(x)
            with open('picture.png', "wb") as f:
                    f.write(frame.content)
            image = iio.imread('picture.png')
            # Emotion detection section
            gray, frame, coordinates = detect_face(image)
            if coordinates is not None:
                process_img = preprocess(gray)
                idx, conf = detect_emotion(process_img)
                class_name = class_names[idx]
                print(type(coordinates))
                await message.channel.send(class_name)
            else:
                await message.channel.send('Nenhum rosto detectado')

        if message.content.startswith('oi'):
            print('Message detected: oi')
            await message.channel.send('Send it!')

        if message.content.startswith('drift'):
            print('Message detected: drift')
            await message.channel.send('Get sideways')
            await message.channel.send(file=discord.File('sideways.jpg'))
 

client.run('secret_key')