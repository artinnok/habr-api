// JS
function requireAll(requireContext) {
  return requireContext.keys().map(requireContext);
}
var modules = requireAll(require.context('./blocks', true, /\.js$/));

// SCSS
require.context('./blocks', true, /\.scss$/);
