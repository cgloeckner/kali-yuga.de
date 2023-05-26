            <div class="item">
                <img class="preview" src="/static/merch/cloths/{{item}}.jpg" />
                <span>
                    <span class="title">{{data['title']}}</span>
%include('merch/price', price=data['price'])
                </span>
            </div>