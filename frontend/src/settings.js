class Settings {
  API_URI
  YANDEX_FORMS_URI

  constructor() {
    this.API_URI = process.env.REACT_APP_API_URI
    if (!this.API_URI)
      throw new Error("REACT_APP_API_URI environment variable wasn't set");

    this.YANDEX_FORMS_URI = process.env.REACT_APP_YANDEX_FORMS_URI
    if (!this.YANDEX_FORMS_URI)
      throw new Error("REACT_APP_YANDEX_FORMS_URI environment variable wasn't set");
  }
}


export const settings = new Settings()

export default settings
