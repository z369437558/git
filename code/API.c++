bool dfs(position1)
    {
        int flag1=0;
        for(j=1 to n)
        {
            if(map1[position1][j]==1)
            {
                count[j]++;
                if(j==b1) 
                {
                    roadcount++;
                    return 0;
                }
                dfs(j);
            }
            
        }
        return 0;
    }
scanf(n,m);
for i=1 to m
    scanf(a,b)
    map1[a][b]=1;
scanf(q)
for i=1 to q
{
    ans=0;
    scanf(a1,b1)
    dfs(a1)
    for(k=1 to n)
    {
        if(count[k]==roadcount)&&(i!=a1)&&(i!=b1) ans++;
        
    }
    printf(ans+2);
}
