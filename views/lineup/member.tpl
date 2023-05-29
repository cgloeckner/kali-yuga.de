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
%if 'projects' in data:
    <div class="projects">auch:
    %for name in data['projects']:
        %include('lineup/project', name=name, url=data['projects'][name])
       %end
    </div>
%end
    </span>
