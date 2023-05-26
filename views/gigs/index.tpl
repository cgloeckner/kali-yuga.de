%include('header')

<div class="gigs">

%years_desc = sorted(data.keys(), key=lambda v: -v)
%for year in years_desc:
    <h2>{{year}}</h2>
    %include('gigs/list', data=data[year])
%end

</div>

%include('footer')
