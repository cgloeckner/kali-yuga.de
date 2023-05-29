%include('header')

<img class="title" src="/content/titles/releases.jpg" />

<div class="releases">

<h1 class="shifted">Releases</h1>

    <div class="container">
%for item in data:
    %include('releases/item', item=item)
%end
    </div>

</div>

%include('footer')
