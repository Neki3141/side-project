#ifndef OPTIONS_H
#define OPTIONS_H

#include <iostream>
#include <vector>
#include <string>


class Options {
public:
  /* Constructors */
  Options(int argc, char * argv[]);
  Options();  // default constructor
  
  /* Accessors 
     All accessors return a value that tells whether a specific option was requested by the user
  */

  bool help() const;
  bool md5() const;
  bool sha_256() const;
  
  /// Contains a vector with file names to process
  const std::vector<std::string>& hash() const;
  
  /* Modifiers */
  // void m_line(bool result);
  // void m_word(bool result);
  // void m_character(bool result);
  // void m_longest_line(bool result);
  // void m_help(bool result);
  // void m_version(bool result);
  // void m_byte(bool result);


  // Parses command-line arguments and replaces the the current values
  // of file names with new, parsed values
  void parse(int argc, char * argv[]);
  
  /* Debug/ helper functions */
  bool verbose() const;
  void print(std::ostream& out) const;

private:
  /* TODO: you fill this part */
  bool help_{false};
  bool md5_{false};
  bool sha_256_{false}; 
  bool verbose_{false};
  std::vector<std::string> hash_{};
};

// you may use this function to print directly to a stream
inline std::ostream& operator<<(std::ostream& out, const Options& opt)
{
  out << "Options: \n"
      << "\tMD5: "        << std::boolalpha << opt.md5() << "\n"
      << "\tSHA-256: "    << std::boolalpha << opt.sha_256() << "\n"
      << "\t help: "      << std::boolalpha << opt.help()
      << "\thashes:" << "\n";
  for (const auto& fn: opt.hash())
  {  
     out << "\t * " << fn << "\n";
  }
  return out;
}

#endif