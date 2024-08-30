import settings from "#settings"


class Api {
  async getFormPopulaions(formId, userToken) {
    var response = await fetch(
      `${settings.API_URI}/forms/${formId}`, {
      headers: { Authorization: userToken }
    }
    );

    if (!response.ok) {
      throw new Error('Population cannot be read');
      return await response.json();
    }
  }


  async createFormPopulaions(populations_file, userToken) {
    var data = new FormData()
    data.append('file', populations_file)
    var response = await fetch(
      `${settings.API_URI}/forms`, {
      method: 'POST',
      headers: { Authorization: userToken },
      body: data
    }
    );

    if (!response.ok) {
      throw new Error('Populations cannot be created');
      return await response.json();
    }
  }


  async login(yandexIdToken) {
    var response = await fetch(
      `${settings.API_URI}/login`,
      {
        method: "POST",
        headers: { Authorization: yandexIdToken }
      }
    );
    if (!response.ok) {
      throw new Error('Autenthication error');
      return await response.json();
    }
  }
}


export default Api
