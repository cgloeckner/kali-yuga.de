            <div class="item">
                <img class="preview" src="{{get_static_url('/content/cloths/' + item['thumbnail'] + '.jpg')}}">
                <span class="title">{{item['title']}}</span>
                <span class="description">{{item['description']}}</span>
%include('merch/price', price=item['price'])
            </div>
