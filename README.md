# demo-serverless-python3
Demo of Serverless framework with AWS using Python

## Commands used
To invoke function locally and show logs.
```zsh
serverless invoke local -f hello
```

To deploy with verbose mode
```zsh
serverless deploy -v
```

To deploy/update function
```zsh
serverless deploy -f hello
```

To invoke function
```zsh
serverless invoke -f hello
```

To show logs of function
```zsh
serverless logs -f hello
```

To remove with verbose mode
```zsh
serverless remove -v
```

## Contributing

Author: Chris Dao (dqcuong93@gmail.com)

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
