export const formatResponse = (text) => {
    return text.split('\n').map((line, index) => {
      const parts = line.split(/(\*\*.*?\*\*)/g).map((part, i) => {
        if (part.startsWith('**') && part.endsWith('**')) {
          return <strong key={i}>{part.slice(2, -2)}</strong>;
        }
        return <span key={i}>{part}</span>;
      });
  
      return <div key={index} className="mb-2">{parts}</div>;
    });
  };