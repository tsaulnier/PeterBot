import random
import bot

theme = ["it", "seems", "today", "that", "all", "you", "see", "is", "violence", "in", "movies",
         "and", "sex", "on", "tv", "but", "where", "are", "those", "good", "old-fashioned", "values", "on",
         "which", "we", "used", "to", "rely", "lucky", "there\'s", "a", "family", "guy", "lucky",
         "there\'s", "a", "man", "who", "positively", "can", "do", "all", "the", "things", "that", "make", "us",
         "laugh", "and", "cry", "he\'s", "a", "family", "guy"]

def get_response(message, channel, currentIndex) -> str:
    p_message = message.lower()
    
    if channel == "Laugh and Cry":
        # if p_message == "index":
        #     return str(currentIndex)
        if p_message != theme[currentIndex]:
            return "D\'oh! You were supposed to say \"" + theme[currentIndex] + "\", wise guy!"
        elif currentIndex != len(theme) - 1:
            bot.currentIndex = currentIndex + 1
        else:
            bot.currentIndex = 0
            
    if p_message == '!help':
        return '`Try typing Hey Peter or Flip Coin`'
    
    if p_message == 'hey peter':
        return 'Hey Joe.'
    
    if p_message == 'hello peter':
        return 'Hey Brian.'
    
    if p_message == 'hey dad':
        return 'Hey Chris.'
    
    if p_message == 'hi dad':
        return 'Hey Meg.'
    
    if p_message == 'giggity':
        return 'Hey Quagmire.'
    
    if p_message == 'what\'s up peter' or p_message == 'sup peter':
        return 'Hey Cleveland.'
    
    if p_message == 'greetings father':
        return 'Hey Stewie.'
    
    if p_message == 'hello mr peter':
        return "Hi Consuela."
    
    if p_message == 'no more lemon pledge':
        return "Go to the store and buy some, Consuela."
    
    if p_message == 'i have no money':
        return "scene cut"
    
    if p_message == 'hi peter' or p_message == 'hi petah' or p_message == 'hi peetah' or p_message == 'hi peeta':
        return 'Hey Lois.'
    
    if p_message == 'nice':
        return 'Freakin\' sweet!'
    
    if p_message == 'flip' or p_message == 'coin flip' or p_message == 'flip coin':
        result = random.randint(0,1000)
        if result > 500:
            return 'Heads'
        elif result > 0:
            return 'Tails'
        elif result == '0':
            return 'Hey Lois, check it out! The coin landed on it\'s side! What now?'