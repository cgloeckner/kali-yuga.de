%include('header', module_name='releases')

<img class="title" alt="Kali Yuga Live Foto" src="{{get_static_url('/content/titles/releases.jpg')}}">

<div class="releases">

<h1 class="shifted">{{module_title}}</h1>

    <div class="container">
%for item in data:
    %include('releases/item', item=item)
%end
    </div>

</div>

%include('footer')
