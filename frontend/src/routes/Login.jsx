import React, { useEffect } from "react";

const Login = () => {
  useEffect(() => {
    try {
      window.YaAuthSuggest.init(
        {
          client_id: 'decde7f956fb4098881bb2f5402ed613',
          response_type: 'token',
          redirect_uri: "https://beaver.love-this-domen.ru"
        },
        'https://examplesite.com'
      )
        .then(({
          handler
        }) => handler())
        .then(data => console.log('Сообщение с токеном', data))
        .catch(error => console.log('Обработка ошибки', error));
    } catch {
      console.log("YandexID is not working");
    }
  })

  return (<div>AAA</div>);
}

export default Login;
