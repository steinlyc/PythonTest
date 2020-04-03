config = {
    'url':'http://210.74.14.79:5052/1.0/app',
    'headers':{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36','Accept': 'application/json, text/plain, */*','Content-Type': 'application/graphql'},
    'params':'''{
     find_article (
      order: "-created_at"
      skip: 0,
      limit: 1000
      where: {
        show: "1",
      }
    ) {
      id
      url
      title
      summary
      content
      author
      thumbnail
      platform
      created_at
      heat
    }
  }''',
    'key':[
        'Maker',
        'Synthetix',
        'Compound',
        'Aave',
        'Uniswap',
        'InstaDAPP',
        'dForce',
        'dydx',
        'Bancor',
        'WBTC',
        'Lightning Network',
        'Set Protocol',
        'DDEX',
        'Kyber',
        'Nuo Network',
        'bZx',
        'RAY',
        'Dharma',
        'Erasure',
        'Augur',
        'Melon',
        'xDai',
        'Veil',
        'Connext',
        'DeFi',
        '跨链',
        '预言机',
        '借贷',
        'DEX',
        '结算',
        '支付',
        '合约',
        '金融',
    ]
}