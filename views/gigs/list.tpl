%for index, show in enumerate(data):
    %alt = '' if index % 2 == 0 else 'alternate'
        <p class="{{alt}}">
            {{show['date'].strftime('%d.%m.%y')}} <b>{{show['title']}}</b>
    %if show['location'] != '':
            ({{show['location']}})
    %end
        </p>
%end
