0. You should first get everything done in the Django Setup tutorial before doing this.
1. Create an `static` subfolder in the main directory with an Corebackend and images sub-folder: `static/CoreBackend/images`
2. Put the snake image in the images folder (ask Ismail for the image).
3. Make sure the `ECS171Backend/settings.py` has this at the end:
```
STATIC_URL = '/static/'  
STATICFILES_DIRS = [  
    BASE_DIR / "static"  
]

```
4. Paste this into the `index.html`:
```
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
    <link rel="preconnect" href="https://fonts.gstatic.com">  
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">  
</head>  
<body style="font-family: Roboto, sans-serif;">  
  
  
{% load static %}  
<img src="{% static 'CoreBackend/images/medical-296434_1280.png' %}" alt="SnakeDoc" style="display: block;margin:auto;width:10em;height:10em">  
  
<h1 style="text-align: center;text-decoration: steelblue underline;color:teal">ECS 171 - Group 4 - Medical OCR</h1>  
  
<div style="width:100%;background-color:cadetblue;color:snow;text-align: center">  
    <h3 style="text-decoration: underline">- Upload Form - </h3>  
    <a href="{% url 'upload' %}">Go to upload page</a>  
  
</div>  
  
<div style="width:100%;background-color:cadetblue;color:snow;text-align: center">  
    <h3 style="text-decoration: underline">- Group Members -</h3>  
  
        <p>Abigail Almanza</p>  
  
        <p>Fidel Castro</p>  
  
        <p>Mohammad Ismail Daud</p>  
  
        <p>Kenneth Du</p>  
  
        <p>Nadia Etemadi</p>  
  
        <p>Wing Lo</p>  
  
        <p>Jessica Ma</p>  
  
        <p>Randal Murphy</p>  
  
        <p>Charrell Sherman</p>  
  
        <p>Min Hee Son</p>  
  
        <p>Michael Xiao</p>  
  
        <p>Tycho Yacub</p>  
  
</div>  
  
<div style="width:100%;background-color:cadetblue;color:snow;text-align: center">  
    <h3 style="text-decoration: underline">- Project Description -</h3>  
    <p>  
        Did you ever hear the tragedy of Darth Plagueis the Wise? No. I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise. He could use the Force to influence the midi-chlorians to create... life. He had such a knowledge of the Dark Side that he could even keep the ones he cared about... from dying.  
        He could actually... save people from death?  
        The Dark Side of the Force is a pathway to many abilities some consider to be unnatural.  
        What happened to him?  
        He became so powerful, the only thing he was afraid of was... losing his power which, eventually of course, he did. Unfortunately, he taught his apprentice everything he knew. And then his apprentice killed him in his sleep. Ironic. He could save others from death... but not himself.  
        Is it possible to learn this power?  
        Not from a Jedi.  
    </p>  
  
</div>  
  
  
<div style="width:100%;background-color:cadetblue;color:snow;text-align: center">  
    <h3 style="text-decoration: underline">- Download Empty Form -</h3>  
    <button>Download</button>  
  
</div>  
  
</body>  
</html>
```
5. Paste this into the `upload.html`:
```
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
    <link rel="preconnect" href="https://fonts.gstatic.com">  
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">  
</head>  
<body style="font-family: Roboto, sans-serif;">  
  
  
{% load static %}  
<img src="{% static 'CoreBackend/images/medical-296434_1280.png' %}" alt="SnakeDoc" style="display: block;margin:auto;width:10em;height:10em">  
  
<h1 style="text-align: center;text-decoration: steelblue underline;color:teal">ECS 171 - Group 4 - Medical OCR</h1>  
  
<div style="width:100%;background-color:cadetblue;color:snow;text-align: center">  
    <h3 style="text-decoration: underline">- Go To Home Page  - </h3>  
    <a href="{% url 'index' %}">Go to home page</a>  
  
</div>  
  
  
<div style="width:100%;background-color:cadetblue;color:snow;text-align: center">  
    <h3 style="text-decoration: underline">- Upload Instructions -</h3>  
    <p>  
        Did you ever hear the tragedy of Darth Plagueis the Wise? No. I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise. He could use the Force to influence the midi-chlorians to create... life. He had such a knowledge of the Dark Side that he could even keep the ones he cared about... from dying.  
        He could actually... save people from death?  
        The Dark Side of the Force is a pathway to many abilities some consider to be unnatural.  
        What happened to him?  
        He became so powerful, the only thing he was afraid of was... losing his power which, eventually of course, he did. Unfortunately, he taught his apprentice everything he knew. And then his apprentice killed him in his sleep. Ironic. He could save others from death... but not himself.  
        Is it possible to learn this power?  
        Not from a Jedi.  
    </p>  
  
</div>  
  
<div style="width:100%;background-color:cadetblue;color:snow;text-align: center">  
    <h3 style="text-decoration: underline">- Upload Form -</h3>  
    <a href="{% url 'edaresults' %}">Upload (Takes you to EDA page and results page after uploading)</a>  
  
</div>  
  
  
</body>  
</html>

```

6. Paste this into the `results.html`:
```
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
    <link rel="preconnect" href="https://fonts.gstatic.com">  
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">  
</head>  
<body style="font-family: Roboto, sans-serif;">  
  
  
{% load static %}  
<img src="{% static 'CoreBackend/images/medical-296434_1280.png' %}" alt="SnakeDoc" style="display: block;margin:auto;width:10em;height:10em">  
  
<h1 style="text-align: center;text-decoration: steelblue underline;color:teal">ECS 171 - Group 4 - Medical OCR</h1>  
  
<div style="width:100%;background-color:cadetblue;color:snow;text-align: center">  
    <h3 style="text-decoration: underline">- Go To Home and Upload Page  - </h3>  
    <a href="{% url 'upload' %}">Go to upload page</a>  
    <br>  
    <br>  
    <a href="{% url 'index' %}">Go to home page</a>  
</div>  
  
  
<div style="width:100%;background-color:cadetblue;color:snow;text-align: center">  
    <h3 style="text-decoration: underline">- EDA Results -</h3>  
    <p>  
        Did you ever hear the tragedy of Darth Plagueis the Wise? No. I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise. He could use the Force to influence the midi-chlorians to create... life. He had such a knowledge of the Dark Side that he could even keep the ones he cared about... from dying.  
        He could actually... save people from death?  
        The Dark Side of the Force is a pathway to many abilities some consider to be unnatural.  
        What happened to him?  
        He became so powerful, the only thing he was afraid of was... losing his power which, eventually of course, he did. Unfortunately, he taught his apprentice everything he knew. And then his apprentice killed him in his sleep. Ironic. He could save others from death... but not himself.  
        Is it possible to learn this power?  
        Not from a Jedi.  
    </p>  
  
</div>  
  
<div style="width:100%;background-color:cadetblue;color:snow;text-align: center">  
    <h3 style="text-decoration: underline">- Download CSV -</h3>  
    <button>Download</button>  
  
</div>  
  
  
</body>  
</html>

```
7. You now have an `UGLY` website. Congrats! 
