    <div class="grouping">
        <div class="toggle">
            <span onClick="toggleCollapse('{{category}}');">
                <h2><span id="{{category}}_button">&#9662;</span> {{data['title']}}</h2>
            </span>
        </div>
        <div class="container" id="{{category}}_container">
%for item in data:
    %if isinstance(data[item], dict):
        %include(f'merch/{category}_item', item=item, data=data[item])
    %end
%end
        </div>
    </div>
