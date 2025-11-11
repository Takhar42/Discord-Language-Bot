import discord
from googletrans import Translator
from discord.ext import commands
from lingua import Language, LanguageDetectorBuilder
import config

intents = discord.Intents.default()
intent = discord.Intents.all()
intents.message_content = True
intent = discord.Intent = True

client = discord.Client(intents=intents)
translator = Translator()

languages = [Language.AFRIKAANS, Language.ALBANIAN, Language.ARABIC, Language.ARMENIAN, Language.AZERBAIJANI, Language.BASQUE, Language.BELARUSIAN, Language.BENGALI, Language.NYNORSK, Language.BOSNIAN, Language.BULGARIAN, Language.CATALAN, Language.CHINESE, Language.CROATIAN, Language.CZECH, Language.DANISH, Language.DUTCH, Language.ENGLISH, Language.ESTONIAN, Language.ESPERANTO, Language.FINNISH, Language.FRENCH, Language.GANDA, Language.GEORGIAN, Language.GERMAN, Language.GREEK, Language.GUJARATI, Language.HEBREW, Language.HINDI, Language.HUNGARIAN, Language.ICELANDIC, Language.INDONESIAN, Language.IRISH, Language.ITALIAN, Language.JAPANESE, Language.KAZAKH, Language.KOREAN, Language.LATIN, Language.LATVIAN, Language.LITHUANIAN, Language.MACEDONIAN, Language.MALAY, Language.MAORI, Language.MARATHI, Language.MONGOLIAN, Language.PERSIAN, Language.POLISH, Language.PORTUGUESE, Language.PUNJABI, Language.ROMANIAN, Language.RUSSIAN, Language.SERBIAN, Language.SHONA, Language.SLOVAK, Language.SLOVENE, Language.SOMALI, Language.SOTHO, Language.SPANISH, Language.SWAHILI, Language.SWEDISH, Language.TAGALOG, Language.TAMIL, Language.TELUGU, Language.THAI, Language.TSONGA, Language.TSWANA, Language.TURKISH, Language.UKRAINIAN, Language.URDU, Language.VIETNAMESE, Language.WELSH, Language.XHOSA, Language.YORUBA, Language.ZULU]
detector = LanguageDetectorBuilder.from_languages(*languages).build()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    print('Online.')

@client.event
async def on_message(message):
    user_message = str(message.content)

    if message.author == client.user:
        return

    if message.content.startswith('!translate'):
        command, *args = message.content.split()

        if len(args) < 2:
            await message.channel.send("Usage: !translate <target_language>(what language you want to translate into) <text_to_translate>(the string or phrase you are trting to translate)")
            return

        target_language = args[0]
        text_to_translate = ' '.join(args[1:])

        try:
            translation = translator.translate(text_to_translate, src='auto', dest=target_language)
            translated_text = translation.text
            await message.channel.send(f"Original message: {text_to_translate}\nTranslated to {target_language}: {translated_text}")
        except Exception as e:
            await message.channel.send("An error occurred while translating. Please try again later.")

    user_lang = detector.detect_language_of(user_message)
    print(user_lang)

TOKEN = input("Enter bot token here: ")

config.params = TOKEN


client.run(TOKEN)
