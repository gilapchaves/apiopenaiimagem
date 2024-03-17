import openai

def acesso():
    openai.api_key = ""
    return openai.api_key

key = acesso()

key = openai.Image.create(
    prompt = "a close up, studio photographic portrait of a white siamese cat that looks curious, backlit ears",
    n = 1,
    size = "1024x1024"
)

print(key)