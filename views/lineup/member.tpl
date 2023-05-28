    <span class="member">
        <img class="portrait" src="/content/lineup/{{key}}.jpg" />
        <div class="name">{{data['name']}}</div>
%if 'nickname' in data:
        <div class="nickname">„{{data['nickname']}}“</div>
%end
%pos = data['position']
%if 'since' in data:
    %pos += f', seit {data["since"]}'
%end
        <div class="position">({{pos}})</div>
%tasks = ', '.join(data['tasks'])
        <div class="tasks">{{tasks}}</div>
    </span>
