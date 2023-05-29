%include('header')

<img class="title" src="/content/titles/gallery.jpg" />

<div class="gallery">

<h1 class="shifted">Gallery</h1>

    <div class="container">
%for file in data:
    %include('gallery/thumbnail', file=file)
%end
    </container>

</div>

%include('footer')