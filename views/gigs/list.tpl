    <table>
    %for index, show in enumerate(data):
        %include('gigs/show', show=show, index=index)
    %end
    </table>
