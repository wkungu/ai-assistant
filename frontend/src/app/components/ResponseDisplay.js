
import {formatResponse} from './utils'

const ResponseDisplay = ({ response }) => {
  return (
    <div className="bg-white shadow-lg rounded-xl p-6 mt-8 max-w-3xl mx-auto">
      <h2 className="text-xl font-semibold mb-4 text-blue-700">Business Advisor Response:</h2>
      <div>{formatResponse(response)}</div>
    </div>
  );
};

export default ResponseDisplay;
