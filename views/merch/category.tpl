    <div class="grouping">
        <div class="toggle">
            <span onClick="toggleCollapse('{{category}}');">
                <h2><span id="{{category}}_button">&#9662;</span> {{category.caption}}</h2>
            </span>
        </div>
        <div class="container" id="{{category}}_container">
%for item in data:
    %include(f'merch/{category}_item', item=item)
%end
        </div>
    </div>
