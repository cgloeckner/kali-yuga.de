            <div class="item">
                <img class="preview" src="/content/cloths/{{item['thumbnail']}}.jpg" />
                <span class="title">{{item['title']}}</span>
%include('merch/price', price=item['price'])
            </div>
