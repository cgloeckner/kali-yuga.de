%include('header', module_name='releases')

<img class="title" src="{{get_static_url('/content/titles/releases.jpg')}}">

<div class="releases">

<h1 class="shifted">Releases</h1>

    <div class="container">
%for item in data:
    %include('releases/item', item=item)
%end
    </div>

</div>

%include('footer')
