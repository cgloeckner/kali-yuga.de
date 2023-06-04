%include('header', get_static_url=get_static_url, module_css='feed')

<img class="title" src="{{get_static_url('/content/titles/feed.jpg')}}">

<div class="feed">

    <img class="large-logo" src="{{get_static_url('/content/logo_inverted.png')}}">

    <h1>KALI YUGA - Official Homepage</h1>

    <div class="elements">

%for key in data:
    %if data[key]['type'] == 'youtube':
        %include('feed/youtube', data=data[key])
    %end
%end
    </div>

</div>

%include('footer')
