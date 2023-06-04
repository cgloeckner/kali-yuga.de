%include('header', module_name='feed')

<img class="title" alt="Kali Yuga Live Foto" src="{{get_static_url('/content/titles/feed.jpg')}}">

<div class="feed">

    <img class="large-logo" alt="Kali Yuga" src="{{get_static_url('/content/logo_inverted.png')}}">

    <h1>KALI YUGA - Death Metal</h1>

    <div class="elements">

%for key in data:
    %if data[key]['type'] == 'youtube':
        %include('feed/youtube', data=data[key])
    %end
%end
    </div>

</div>

%include('footer')
