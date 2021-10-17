# Weather_app
This app was created to access the weather of a given city by the user. To do so, I used https://openweathermap.org/ API to fetch the information.

## Lessons Learned
In this project I learned about REST APIs and how to access and use the data they provide. I also familiarized myself with the APIs documentation and I applied and learn a lot abut the datetime library in python.
Finally, I notice that the app runs a bit slow as it has to access the API everytime, so for a more efficient project, the data should be fetched first and then
stored in a database and finally used in the app.


## Run Locally

Clone the project

```bash
  git clone https://github.com/rebecalvarezc/weatherapp.git
```

Go to the project directory

```bash
  cd weatherapp\ app.py
```

Install dependencies

```bash
  npm install requests
```


## API Reference
Please remember that api_keys are private, so I decided not to share mine in this repository.
#### Get item

```http
  GET /api/weather?q={city_name}&appid={api_key}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |
|`city_name`| `string` | **Required**. city to fetch|

## Authors

- [@rebecalvarezc](https://github.com/rebecalvarezc)

  
