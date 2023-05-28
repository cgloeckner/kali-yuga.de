%for index, show in enumerate(data):
    %alt = '' if index % 2 == 0 else 'alternate'
        <p class="{{alt}}">{{show['date'].strftime('%d.%m.%y')}} ({{show['location']}}) {{show['title']}}</p></li>
%end
