%description = 'Bei den Auftritten der Geraer Death Metal Band KALI YUGA sind zahlreiche Bilder entstanden, von denen hier eine Auswahl zu finden ist.'
%include('header', module_name='gallery')

<img class="title" alt="Kali Yuga Live Foto" src="{{get_static_url('/content/titles/gallery.jpg')}}">

<div class="gallery">

<h1 class="shifted">{{module_title}}</h1>

    <div class="container">
%for file in data:
    %include('gallery/thumbnail', file=file)
%end
    </div>

    <p class="center">Die Urheberrechte der Bilder liegen bei den jeweiligen Fotografen. Wir bedanken uns für die
        Genehmigung zur Nutzung.</p>

</div>

%include('footer')
