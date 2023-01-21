from django import forms


class Edit_Voting_Form(forms.Form):
    title = forms.CharField(label='your title', required=True) # редактирование названия, вместо 'your title' позже поставить уже имеющееся заголовок
    text = forms.CharField(label='your text', required=True) # редактирование описания, вместо 'your text' позже поставить уже имеющейся текст голосования
    number_of_options = forms.DurationField(label= 2, required=True) # количество вариантов для голосования
    type_of_options = forms.CharField(label= 'MultipleChoiceField or ChoiceField', required=True) # тип голосования: множественный или одиночный выбор

    field_of_options = []  # масив полей для голосования, должен ссылаться на то, что уже есть
    for i in range(number_of_options):
        field_of_options.append(forms.ChoiceField()) # в зависимости от типа голосования добавлять разные данные в список
        #field_of_options.append(forms.MultipleChoiceField())

    text_of_options = [] # масив описания полей для голосования, должен ссылаться на то, что уже есть
    for i in range(number_of_options):
        text_of_options.append(forms.CharField(label='')) # сам текст хранится здесь

    # не уверен, что циклы должны выглядеть так и находиться здесь
