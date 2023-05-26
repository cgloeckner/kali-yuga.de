    <table>
        <tr>
            <th></th>
            <th></th>
            <th></th>
        </tr>
    %for show in data:
        %include('gigs/show', show=show)
    %end
    </table>
