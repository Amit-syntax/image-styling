import requests



def main():
    files = [
        {'image1': open('test-img.jpg', 'rb')},
        {'image1': open('img-2.png', 'rb')},
        {'image1': open('img-3.png', 'rb')},
    ]
    for fl in files:
        req = requests.post('http://127.0.0.1:5000/image/edit', files=fl, data={
            "style": """
            image1{
                blur:10;
                brightness: 1;
                resize:  1000,1000;
            }
            """
        })
    
        print(req.json())


if __name__ == '__main__':
    
    print('running')
    main()