const loginForm = document.getElementById('login-form');
const searchInput = document.getElementById('search-input');
const content = document.getElementById('content');
const baseEndpoint = 'http://localhost:8000/api';

function fetchData({ method, url, payload, accessToken }) {
  const options = {
    method: method === null ? 'GET' : method,
    headers: {
      'Content-Type': 'application/json',
    },
  };

  if (payload) options.body = JSON.stringify(payload);

  if (accessToken) options.headers.Authorization = `Bearer ${accessToken}`;

  return fetch(url, options)
    .then((res) => {
      const { status } = res;
      if (status === 401) return res;
      if (status === 403) return res;
      return res.json();
    })
    .then((data) => data);
}

if (loginForm) {
  loginForm.addEventListener('submit', handleLogin);
}

if (searchInput) {
  searchInput.addEventListener('input', handleSearch);
}

async function handleLogin(e) {
  e.preventDefault();
  const loginFormData = new FormData(e.target);
  const loginObj = Object.fromEntries(loginFormData);

  const loginEndpoint = `${baseEndpoint}/token/`;
  const response = await fetchData({
    method: 'POST',
    url: loginEndpoint,
    payload: loginObj,
  });
  handleAuthData(response);
}

async function handleSearch(e) {
  if (e.target.value !== '') {
    const endpoint = `${baseEndpoint}/products/search/?q=${e.target.value}`;

    fetchData({
      method: 'GET',
      url: endpoint,
    }).then((res) => {
      let isValid = true;
      isTokenValid().then((res) => (isValid = res));
      if (isValid && content) {
        if (res && res.hits.length > 0) {
          let htmlStr = '';
          content.innerHTML = '';
          for (const hit of res.hits) {
            htmlStr += `<li key={${hit.objectID}}>${hit.title}</li>`;
          }
          content.innerHTML += `${htmlStr}`;
        } else {
          content.innerHTML = '<p>No results found</p>';
        }
      }
    });
  } else {
    getProductList();
  }
}

function handleAuthData(token) {
  if (token.access && token.refresh) {
    localStorage.setItem('access', token.access);
    localStorage.setItem('refresh', token.refresh);
  }
  getProductList();
}

function writeToContent(data) {
  if (content) {
    content.innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
  }
}

async function getProductList() {
  const endpoint = `${baseEndpoint}/products/`;
  const response = await fetchData({
    url: endpoint,
    accessToken: localStorage.getItem('access'),
  });

  if (response.status === 403) {
    refreshToken();
  } else {
    writeToContent(response);
  }
}

async function refreshToken() {
  const endpoint = `${baseEndpoint}/token/refresh/`;
  const response = await fetchData({
    method: 'POST',
    url: endpoint,
    payload: { refresh: localStorage.getItem('refresh') },
  });

  if (response.access) {
    localStorage.setItem('access', response.access);
    getProductList();
  }
}

async function isTokenValid() {
  const endpoint = `${baseEndpoint}/token/verify/`;
  const response = await fetchData({
    method: 'POST',
    url: endpoint,
    payload: { token: localStorage.getItem('access') },
  });

  if (response.status === 401) return false;
  return true;
}

getProductList();

isTokenValid().then((res) => {
  if (res) console.log('VALIDO');
  else console.log('INVALIDO');
});
