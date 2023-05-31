%include('header', get_static_url=get_static_url)

<img class="title" src="/content/titles/gallery.jpg">

<div class="gallery">

<h1 class="shifted">Gallery</h1>

    <div class="container">
%for file in data:
    %include('gallery/thumbnail', file=file)
%end
    </div>

</div>

%include('footer')