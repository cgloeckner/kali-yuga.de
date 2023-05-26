%include('header')

<div class="merch">

%for category in data:
    %include('merch/category', category=category, data=data[category])
%end

</div>

%include('footer')
