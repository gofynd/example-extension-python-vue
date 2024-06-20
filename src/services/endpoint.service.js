import urlJoin from "url-join";
import root from "window-or-global";
let envVars = root.env || {};

envVars.EXAMPLE_MAIN_URL = `${root.location.protocol}//${root.location.hostname}`;
// envVars.EXAMPLE_MAIN_URL = `${root.location.protocol}//${root.location.hostname}:${root.location.port}`;
if (
  root &&
  root.process &&
  root.process.env &&
  root.process.NODE_ENV == "test"
) {
  envVars.EXAMPLE_MAIN_URL = 'https://api.xyz.com';
}

const Endpoints = {
  GET_TEST_API() {
    return urlJoin(envVars.EXAMPLE_MAIN_URL, '/api/v1.0/test-api')
  },
  GET_ALL_PRODUCTS(){
    return urlJoin(envVars.EXAMPLE_MAIN_URL, '/api/v1.0/products')
  },
  GET_ALL_APPLICATION_PRODUCTS(applicationId) {
    return urlJoin(envVars.EXAMPLE_MAIN_URL, `/api/v1.0/${applicationId}/products`)
  }
};

export default Endpoints;