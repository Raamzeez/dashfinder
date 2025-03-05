def filter_model(model_name, company_name):
    split_text = model_name.split(" ")
    i = 1
    if (split_text[0].lower() == company_name.lower()):
        model_name = ""
        while (i < len(split_text)):
            model_name += split_text[i]
            if (i < len(split_text) - 1):
                model_name += " "
            i += 1
    return model_name
