%include('header')

<img class="title" src="/content/titles/gallery.jpg" />

<div class="gallery">

<h1 class="shifted">Gallery</h1>

    <div class="container">
%for file in data:
        <div class="thumbnail">
            <a href="/content/gallery/{{file}}" target="_blank">
                <img src="/content/gallery/{{file}}" />
            </a>
        </div>
%end
    </container>

</div>

%include('footer')