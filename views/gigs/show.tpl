%alt = '' if index % 2 == 0 else 'alternate'
        <tr>
            <td class="date {{alt}}">{{show['date'].strftime('%d.%m.%y')}}</td>
            <td class="title {{alt}}">{{show['title']}}</td>
            <td class="location {{alt}}">{{show['location']}}</td>
        </tr>
