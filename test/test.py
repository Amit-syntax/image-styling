import requests



def main():
    files = {
        'image1': open('test-img.jpg', 'rb')
    }
    req = requests.post('http://127.0.0.1:5000/image/edit', files=files, data={"some": "sef"})
    
    print(req.json())


if __name__ == '__main__':
    
    print('running')
    main()