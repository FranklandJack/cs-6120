# [Lesson 2: Representing Programs](https://www.cs.cornell.edu/courses/cs6120/2022sp/lesson/2/)

Tasks:

Your goal is to get familiar with [Bril](https://github.com/sampsyo/bril).

- [x] Write a new benchmark.
      * You can write it by hand, use the [TypeScript
        compiler](https://capra.cs.cornell.edu/bril/tools/ts2bril.html), or
        generate it some other way.
      * Try running it with
        [brili](https://capra.cs.cornell.edu/bril/tools/brilirs.html).
      * Open a pull request to add your new benchmark.
          * Add your code to the [the benchmarks
            directory](https://github.com/sampsyo/bril/tree/main/benchmarks).
          * Use turnt --save yours.bril to create the test outputs for your new
            benchmark. (See the [Turnt](https://github.com/cucapra/turnt) README for details.)
          * If your @main function takes arguments, you can specify ones to use
            in testing with an ARGS: comment, [like
            this](https://github.com/sampsyo/bril/blob/06ed7bd18324fbb8902f1ebc43fd71deac8bfb03/benchmarks/fizz-buzz.bril#L1-L2).
          * Mention it in [the docs](https://github.com/sampsyo/bril/blob/main/docs/tools/bench.md).
- [x] Write a program to analyze or transform Bril programs in some small way.
      *  Pick your favorite programming language—there is no “starter code,” so
         you can start from scratch.
      *  Load up a JSON file. You can start with [this tiny
         one](https://github.com/sampsyo/bril/blob/main/test/parse/add.json)!
      *  Read [the docs](https://capra.cs.cornell.edu/bril/).
      *  Do something unambitious with it: count the number of add
         instructions, or add a print instruction before every jump, or
         whatever. Pick something small and contrived!
- [x] Use [Turnt](https://github.com/cucapra/turnt) to test your new tool.
- [x] Along the way, you will run into problems! Ask questions on
  [Zulip](https://cs6120.zulipchat.com/), and open issues and pull requests to
  describe or fix problems. For example, even
  super simple benchmarks you might imagine probably can’t be written easily
  because Bril is too simple. Mention this on Zulip, and consider pitching in
  to help add features.
- [x] As with all implementation tasks, submit the URL for your source code on
  [CMS](https://cmsx.cs.cornell.edu/).
