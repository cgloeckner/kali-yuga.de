%include('header')

<img class="title" src="/content/titles/feed.jpg">

<div class="feed">

    <img class="large-logo" src="/content/logo_inverted.png">

    <div class="elements">
%for key in data:
    %if data[key]['type'] == 'youtube':
        %include('feed/youtube', data=data[key])
    %end
%end
    </div>

</div>

%include('footer')
