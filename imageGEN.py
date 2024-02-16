import openai
def imageGeneration(prompt):
    api_key = "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"
    openai.api_key = api_key
    response = openai.Image.create(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    image_url = response.data[0].url
    return image_url
print(imageGeneration(" "))