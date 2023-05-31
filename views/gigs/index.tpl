%include('header')

<img class="title" src="/content/titles/gigs.jpg">

<div class="gigs">

<h1 class="shifted">Live Shows</h1>

<p class="center"><a href="mailto:{{booking_email}}">{{booking_email}}</a></p>

%years_desc = sorted(data.keys(), key=lambda v: -v)
%for year in years_desc:
    <div class="list">
        <h2>{{year}}</h2>
        %include('gigs/list', data=data[year])
    </div>
%end

</div>

%include('footer')
