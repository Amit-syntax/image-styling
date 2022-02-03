import pathlib
from PIL import Image, ImageFilter, ImageEnhance
import cssutils


def parse_rules(style: str):
    
    sheet = cssutils.parseString(style)
    rulesText = sheet.cssRules[0].style.cssText
    
    rules = []
    
    for rule in rulesText.split(';'):
        if rule.strip():
            name = rule.split(':')[0]
            value = rule.split(':')[1]
            rules.append({
                'name': name.strip(),
                'value': value.strip()
            })

    return rules
    

def style_image(path: pathlib.Path, style: str):
    """styles calls filters and styles as per given style.

    Args:
        path (pathlib.Path): path of the image.
        style (str): style of image.
    """
    
    executor_dict = {
        'blur': blur,
        'brightness' : brightness,
        'resize' : resize,
    }
    
    rules = parse_rules(style)
    image = Image.open(open(str(path.absolute()), 'rb'))

    for rule in rules:
        try:
            image = executor_dict[rule['name']](image, rule['value'])
        except KeyError:
            pass
    
    return image

def blur(image: Image, blur_value):
    
    return image.filter(ImageFilter.BoxBlur(int(blur_value)))


def brightness(image: Image, brightness_value):

    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(int(brightness_value))


def resize(image: Image, value: str):
    h,w = value.split(',')
    
    return image.resize((int(h), int(w)))