from django.http import HttpResponse
from django.shortcuts import render
import string

def home(request):
    return render(request, 'home.html')

def landing(request):
        # Text which Is Received From Text Box
    text_received = request.POST.get('text_carrier','Empty String')
    # Variable To Save State Of Button Punctuation ie On Or Off, Default Value Is Off 
    button_state_punctuation = request.POST.get('button_to_remove_punctuation','off')
    # Variable To Save State Of Button Capitalize ie On Or Off, Default Value Is Off
    button_state_capitalize = request.POST.get('button_to_capitalize', 'off')
    # Variable To Save State Of Button Newline Remover ie On Or Off, Default Value Is Off
    button_state_newline = request.POST.get('button_to_remove_newline', 'off')
    # Variable To Save State Of Button Character Counter ie On Or Off, Default Value Is Off
    button_state_chracter_counter = request.POST.get('button_to_count_character', 'off')

    text_without_punctuation = ''
    processed_data = ''
    char_counter = ''

    # Condition To Check Punctuation and Capitalize Is On
    if button_state_capitalize == 'on' and button_state_punctuation == 'on':
        text_without_punctuation = text_received.upper()
        # Condition To Check Punctuation is on And Remove Punctuation Logic    
        for text in text_without_punctuation:
            if text not in string.punctuation:
                processed_data += text
     # Condition To Check Only Capitalize is on
    elif button_state_capitalize == 'on':
        processed_data = text_received.upper()
    # Condition To Check Only Punctuation is on
    elif button_state_punctuation == 'on':
        for text in text_received:
            if text not in string.punctuation:
                processed_data += text
    # Condition To Check Newline Reomver is on
    elif button_state_newline == 'on':
        for text in text_received:
            if text != '\n' and text !='\r':
                processed_data += text
    # Condition To Count Character In String
    elif button_state_chracter_counter == 'on':
        char_counter = f'The Length Of Your Enter Text Is {len(text_received)}'
    # Condition if both are off     
    else:
        processed_data = f'Please Check Any Checkbox For Text Processing On This String 👉🏼 {text_received}'
    params = {'work_done' : 'Processed Text Is 👇🏼', 'processed_data' : processed_data, 'text_size' : char_counter}
    return render(request, 'landing.html', params)