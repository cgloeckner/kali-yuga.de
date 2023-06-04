%include('header', module_name='gallery')

<img class="title" src="{{get_static_url('/content/titles/gallery.jpg')}}">

<div class="gallery">

<h1 class="shifted">Gallery</h1>

    <div class="container">
%for file in data:
    %include('gallery/thumbnail', file=file)
%end
    </div>

</div>

%include('footer')