const App = () => {
  return (
    <div className="flex flex-col items-center min-h-screen w-screen p-8 bg-white bg-[url('https://img.freepik.com/free-vector/winter-blue-pink-gradient-background-vector_53876-117276.jpg?t=st=1740857092~exp=1740860692~hmac=fd7b403492528b286fb4a6dc352b5c34cf1df0b8fd0777b20d649e0aa2a1235c&w=2000')] bg-cover bg-center">
      <h1 className="text-2xl font-semibold text-gray-700">
        Enter Vehicle Name
      </h1>
      <input
        type="text"
        className="min-w-80 w-1/2 bg-gray-100 shadow-sm border-none rounded-xl p-4 outline-none my-10 h-10"
      />
    </div>
  );
};

export default App;
